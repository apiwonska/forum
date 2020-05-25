import fetchCategories from './categoriesActions';

export {
  register,
  logIn,
  logOut,
  resetPassword,
  confirmPasswordReset,
  changePassword,
} from './authActions';
export { fetchCategories };
export {
  fetchThreadsByCategory,
  fetchThread,
  createThread,
} from './threadsActions';
export {
  fetchPostsByThread,
  fetchPostsByUser,
  createPost,
  updatePost,
  deletePost,
} from './postsActions';
export { fetchUser, updateUser, uploadAvatar } from './usersActions';
