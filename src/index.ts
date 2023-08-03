import express, { Application, Request, Response } from 'express';
import fibonacci from './services/fibonacci';
import * as JSONBig from 'json-bigint';

const app: Application = express();

app.get('/', async (req: Request, res: Response): Promise<Response> => {
  return res.status(200).send({
    message: 'Hello World!',
  });
});

app.get('/fib', async (req: Request, res: Response): Promise<Response> => {
  const { n } = req.query;
  let fibResult: bigint | undefined;
  if (!n) {
    return res.status(400).send({ status: 400, message: 'Query parameter is required' });
  }

  try {
    fibResult = await fibonacci(Number(n));
  } catch (err: unknown) {
    if (err instanceof Error) {
      return res.status(400).send({ status: 400, message: err.message });
    }
  }

  const r = JSONBig.parse(`{ "result": ${fibResult} }`);
  console.log(r.result.toString());
  return res.status(200).send(r);
});

app.listen(3000, (): void => {
  console.log('Server is running on port 3000');
});

export default app;
