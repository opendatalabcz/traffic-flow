import { HttpClient } from './http-client';
import { Task } from '../types';

export class TaskClient extends HttpClient {
  public constructor() {
    super('http://localhost:8000/task');
  }

  public getTask = (taskId: number) => this.instance.get<Task>(`${taskId}`).then(response => response.data);

  public getVisualization = (taskId: number) =>
    this.instance.get(`${taskId}/visualization`, { responseType: 'blob' }).then(response => response.data);
}
