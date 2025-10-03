import { APIUtils } from "../../.server";
import { ACTION_CONST } from "../../utils";
import type { ProductIndexActionPropTypes } from "./types";

const getGetProjects = async (
  values: Record<string, FormDataEntryValue>,
  request: Request,
): Promise<ProductIndexActionPropTypes> => {

  const tags: string[] = []
  const catgories: string[] = []

  Object.keys(values).forEach((key) => {
    if (key.includes('tag-') && typeof values[key] === 'string') tags.push(values[key])
    if (key.includes('category-') && typeof values[key] === 'string') catgories.push(values[key])
  })

  const params = []

  if (tags.length > 0) params.push(`tags=${tags.join(',')}`)
  if (catgories.length > 0) params.push(`catgories=${catgories.join(',')}`)
  if (values.search && typeof values.search === 'string') params.push(`search=${values.search}`)

  const url = params.length > 0 ? `product?${params.join('&')}` : 'product';

  const { result } = await APIUtils.fetchHandler('GET', url, { request })
  console.log('🚀 ~ getGetProjects ~ result:', result);

  return {
    products: result.products
  }
}

export const productIndexActionHandler = async (request: Request): Promise<ProductIndexActionPropTypes> => {
  const formData = await request.formData();
  const { _action, ...values } = Object.fromEntries(formData);

  switch (_action) {
    case ACTION_CONST.GET_PROJECTS:
      return getGetProjects(values, request);

    default:
      return {
        errors: 'Invalid action type'

      };
  }
}