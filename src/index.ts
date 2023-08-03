import express, { Application, Request, Response } from 'express';

const app: Application = express();

app.get('/', async (req: Request, res: Response): Promise<Response> => {
  return res.status(200).send({
    message: 'Hello World!',
  });
});

app.listen(3000, (): void => {
  console.log('Server is running on port 3000');
});

export default app;
