type MethodTypes = 'POST' | 'GET' | 'PUT' | 'PATCH' | 'DELETE';

export class APIUtils {
  constructor() { }

  static async fetchHandler (
    method: MethodTypes,
    path: string,
    options?: {
      values?: any,
      request?: Request,
      accessToken?: string,
      isFormData?: boolean,
    },
  ) {

    const body = options?.values ? options.isFormData ? options?.values : JSON.stringify(options.values) : undefined;

    const headers: Record<string, string> = {
      Accept: 'application/json',
    };

    if (!options?.isFormData) {
      headers['Content-Type'] = 'application/json';
    }

    const response = await fetch(`http://localhost:8000/${path}`, {
      method: method,
      headers,
      body,
    });

    if (response.status === 204) return { success: true };
    if (response.status === 404) return { success: false };

    const result = await response.json();

    return { result, success: true };
  }
}