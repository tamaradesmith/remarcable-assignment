import { APIUtils } from "../../.server";
import type { ProductIndexLoaderPropTypes } from "./type";

export const ProductIndexLoader = async (request: Request): Promise<ProductIndexLoaderPropTypes> => {
  const [
    products,
    filterOptions,
  ] = await Promise.all([
    await APIUtils.fetchHandler('GET', 'product', { request }),
    await APIUtils.fetchHandler('GET', 'product/product_filter_options', { request })
  ])

  return {
    products: products.result.products,
    filters: {
      categories: filterOptions?.result.categories || [],
      tags: filterOptions?.result.tags || [],
    }
  }
}