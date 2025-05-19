import os
from typing import List
from langchain_community.document_loaders.unstructured import validate_unstructured_version
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
#-*- conding:utf-8 -*-
 
    

class DocLoader(UnstructuredWordDocumentLoader):
    """
    继承官方UnstructuredWordDocumentLoader方法，重写load操作使其符合中文行文习惯，暂时没法改进，之后
    """
    def _get_elements(self) -> List:
        from unstructured.file_utils.filetype import FileType, detect_filetype
        # NOTE(MthwRobinson) - magic will raise an import error if the libmagic
        # system dependency isn't installed. If it's not installed, we'll just
        # check the file extension
        try:
            import magic  # noqa: F401

            is_doc = detect_filetype(self.file_path) == FileType.DOC  # type: ignore[arg-type]
        except ImportError:
            _, extension = os.path.splitext(str(self.file_path))
            is_doc = extension == ".doc"

        if is_doc:
            validate_unstructured_version("0.4.11")

        if is_doc:
            from unstructured.partition.doc import partition_doc

            return partition_doc(filename=self.file_path, **self.unstructured_kwargs)  # type: ignore[arg-type]
        else:
            from unstructured.partition.docx import partition_docx

            return partition_docx(filename=self.file_path, **self.unstructured_kwargs)  # type: ignore[arg-type]
        


if __name__ == "__main__":
    loader = DocLoader(file_path=r"/home/xwt2gpu/E/xwt_server/llm_rag_server_v1.0.0/doc/幽门螺杆菌感染基层诊疗指南（2019 年）.docx")
    docs = loader.load()
    print(docs)
