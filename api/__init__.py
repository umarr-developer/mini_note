import fastapi
from api.users.views import router as user_router
from api.notes.views import router as note_router

router = fastapi.APIRouter(prefix='/api')
router.include_router(user_router)
router.include_router(note_router)
