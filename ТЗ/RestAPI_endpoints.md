Workspaces

GET /api/workspaces — список

POST /api/workspaces — создать {name, description}

GET /api/workspaces/{id} — получить

PATCH /api/workspaces/{id} — обновить

DELETE /api/workspaces/{id} — удалить (cascade)

Documents

GET /api/workspaces/{ws_id}/documents — список документов

POST /api/workspaces/{ws_id}/documents — загрузка файла (multipart)

GET /api/documents/{doc_id} — метаданные/статус

DELETE /api/documents/{doc_id} — удалить

Чаты

GET /api/workspaces/{ws_id}/chats — список чатов

POST /api/workspaces/{ws_id}/chats — создать чат {title?}

GET /api/chats/{chat_id} — инфо чата

GET /api/chats/{chat_id}/messages — история

POST /api/chats/{chat_id}/messages — отправить user message {content}

RAG Chat (основное)

POST /api/chats/{chat_id}/ask

body:

{
  "question": "Какие штрафы по договору?",
  "top_k": 6,
  "mode": "grounded", 
  "temperature": 0.2
}

response:

{
  "answer": "...",
  "sources": [
    {
      "chunk_id": "...",
      "document_id": "...",
      "filename": "contract.pdf",
      "page_number": 4,
      "snippet": "..."
    }
  ]
}