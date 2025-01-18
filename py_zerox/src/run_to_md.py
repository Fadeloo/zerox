import os
import asyncio
from dotenv import load_dotenv
from typing import Optional, Union, Iterable
from pyzerox import zerox  # 从 pyzerox 导入 zerox 函数

# 从 .env 文件加载 API 密钥
load_dotenv()  # 加载当前目录下的 .env 文件
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")  # 从 .env 文件获取 OPENAI_API_KEY

# 遍历目录中的所有文件并处理
async def process_model(
    cleanup: bool = True,
    concurrency: int = 10,
    file_path: Optional[str] = "inputfile",  # 默认文件夹路径 "inputfile"
    maintain_format: bool = False,
    model: str = "gpt-4o-mini",
    output_dir: Optional[str] = "outputfile",  # 默认输出文件夹路径 "outputfile"
    temp_dir: Optional[str] = None,
    custom_system_prompt: Optional[str] = None,
    select_pages: Optional[Union[int, Iterable[int]]] = None,
    **kwargs
):
    """
    异步处理 inputfile 文件夹中的所有文件，使用指定模型进行推理。
    """
    # 获取 inputfile 文件夹中的所有文件
    files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
    
    # 逐个处理文件
    for file_name in files:
        file_to_process = os.path.join(file_path, file_name)
        
        print(f"Processing file: {file_to_process}")

        try:
            # 调用 zerox 函数进行文件处理
            result = await zerox(
                cleanup=cleanup,
                concurrency=concurrency,
                file_path=file_to_process,
                maintain_format=maintain_format,
                model=model,
                output_dir=output_dir,
                temp_dir=temp_dir,
                custom_system_prompt=custom_system_prompt,
                select_pages=select_pages,
                **kwargs
            )
            print(f"Processing result for {file_name}: {result}")

        except Exception as e:
            print(f"An error occurred while processing {file_name}: {str(e)}")

# 运行主函数
async def main():
    await process_model()

# 启动异步主函数
if __name__ == "__main__":
    asyncio.run(main())
