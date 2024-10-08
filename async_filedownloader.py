async def download_file(file_name: str, url: str, chunk_size: int = 1024 * 1024, max_retries: int = 10) -> None: # 1024 * 1024 = 1Mb по умолчанию
  """
  Асинхронный почанковый даунлоадер с прогрессбаром и возможностью докачки.

	:param file_name: имя файла
	:param url: ссылка на файл
	:param chunk_size: размер блока для скачивания
	:param max_retries: максимальное количество повторных попыток
	"""
	file_exists = os.path.exists(file_name)
	local_size = os.path.getsize(file_name) if file_exists else 0
	file_mode = 'ab' if file_exists else 'wb'

	timeout = aiohttp.ClientTimeout(total=600)
	retries = 0

	while retries < max_retries:
		try:
			async with aiohttp.ClientSession(timeout=timeout) as session:
				async with session.get(url, headers=headers, raise_for_status=True) as response:
					total_size = int(response.headers.get('Content-Length', 0))
					
					if total_size == 0:
						print("Content-Length не определен. Скачивание без progress bar...")
						with open(file_name, file_mode) as file:
							while True:
								chunk = await response.content.readany()
								if not chunk:
									break
								file.write(chunk)
						return


					with open(file_name, file_mode) as file:
						with tqdm(total=total_size, unit='B', unit_scale=True, desc=file_name, initial=local_size) as pbar:
							async for chunk in response.content.iter_chunked(chunk_size):
								file.write(chunk)
								pbar.update(len(chunk))
							return

		except (asyncio.TimeoutError, aiohttp.ClientError, aiohttp.ClientPayloadError) as e:
			retries += 1
			wait_time = random.uniform(2, 5)
			print(f"Ошибка: {e} при скачивании {url}. Повторная попытка {retries} через {wait_time:.1f} секунд...")
			await asyncio.sleep(wait_time)

	print(f"Ошибка: Не удалось скачать файл {url} после {max_retries} попыток.")
