
- [ ] POST /images
    - [x] Enpoint must allow to upload an image in commonly used image formats.
    - [x] Endpoint must allow for setting image title
    - [x] Image object must be stored in database
    - [x] Image file must be stored in storage (see Requirements)
    - [x] Image should be resized according to width and height parameters provided in request

- [ ] GET /images
    - [x] Endpoint must return a list of image objects with their respective id, url, title, width and height
    - [x] Endpoint should allow for filtering based on title - "title must contain {text}"
    - [x] Enpoint should include pagination

-[ ] GET /images/:id
    - [ ] Endpoint should return single image object with their respective id, url, title, width and height based on provided id


- [x] Dev environment - docker(-compose), virtualenv
- [ ] Storage - filesystem or external storage (Amazon S3, Azure Storage, Gogole Storage)
- [x] Image processing - image should be scaled or cropped and optimized to given size
- [x] API Documentation - OpenAPIv3 (swagger)
- [ ] Dev documentation (readme.md)


Review
The application's code can be hosted as a public repository, or private repository with READ access to the reviewers - their emails or usernames should be provided in the email you received this task with.
If you have any questions feel free to ask - we are availbile via the same email addresses as reviewers :)
Good luck :)