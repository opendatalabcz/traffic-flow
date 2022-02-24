import { OutputType } from './enums';

export type Line = {
  name: string;
  start: Point;
  end: Point;
};

export type Lines = {
  id: number;
  task_id: number;
  lines: Line[];
};

export type Point = {
  x: number;
  y: number;
};

export type SourceFile = {
  id: number;
  name: string | undefined;
  path: string;
  status: string;
  file_exists: boolean;
};

export type SourceFileWithTasks = SourceFile & {
  tasks: Task[];
};

export type Task = {
  id: number;
  source_file_id: number;
  output_method: OutputType;
  output_path: string;
  status: string;
  models: string[];
  parameters: { [id: string]: string | number };
  lines: Lines[];
};
