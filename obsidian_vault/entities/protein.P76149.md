---
entity_id: "protein.P76149"
entity_type: "protein"
name: "sad"
source_database: "UniProt"
source_id: "P76149"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sad yneI b1525 JW5247"
---

# sad

`protein.P76149`

## Static

- Type: `protein`
- Source: `UniProt:P76149`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NAD(+)-dependent oxidation of succinate semialdehyde to succinate. It acts preferentially with NAD as cosubstrate but can also use NADP. Prevents the toxic accumulation of succinate semialdehyde (SSA) and plays an important role when arginine and putrescine are used as the sole nitrogen or carbon sources. {ECO:0000269|PubMed:17873044, ECO:0000269|PubMed:20639325, ECO:0000269|PubMed:7009588, ECO:0000269|PubMed:7011797}. E. coli K-12 encodes two succinate semialdehyde dehydrogenases, Sad and CPLX0-7688 "GabD", which differ in their ability to utilize NAD+ and NADP+. Sad is the smaller enzyme and preferentially utilizes NAD+ ; the gene encoding it was long unknown. Sad also functions as a glutarate semialdehyde dehydrogenase during degradation of L-lysine . YneI was found to be identical to the orphan enzymatic activity of NAD+-dependent succinate semialdehyde dehydrogenase (Sad). Its activity was first predicted using phylogenetic profiles and later confirmed biochemically . Sad has an important role during growth on arginine and is likely required for growth on putrescine as the sole source of nitrogen. Its main function may be to prevent accumulation of the toxic compound succinate semialdehyde . Sad is more important than GabD for growth on putrescine as the sole source of carbon...

## Biological Role

Catalyzes succinate-semialdehyde:NAD+ oxidoreductase (reaction.R00713), succinate-semialdehyde:NADP+ oxidoreductase (reaction.R00714). Component of succinate semialdehyde dehydrogenase (NAD(P)+) Sad (complex.ecocyc.CPLX0-7687).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the NAD(+)-dependent oxidation of succinate semialdehyde to succinate. It acts preferentially with NAD as cosubstrate but can also use NADP. Prevents the toxic accumulation of succinate semialdehyde (SSA) and plays an important role when arginine and putrescine are used as the sole nitrogen or carbon sources. {ECO:0000269|PubMed:17873044, ECO:0000269|PubMed:20639325, ECO:0000269|PubMed:7009588, ECO:0000269|PubMed:7011797}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00713|reaction.R00713]] `KEGG` `database` - via EC:1.2.1.16
- `catalyzes` --> [[reaction.R00714|reaction.R00714]] `KEGG` `database` - via EC:1.2.1.16
- `is_component_of` --> [[complex.ecocyc.CPLX0-7687|complex.ecocyc.CPLX0-7687]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1525|gene.b1525]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76149`
- `KEGG:ecj:JW5247;eco:b1525;ecoc:C3026_08815;`
- `GeneID:947440;`
- `GO:GO:0004030; GO:0004777; GO:0006099; GO:0006527; GO:0009013; GO:0009447; GO:0009450; GO:0036243; GO:0042803; GO:0070458`
- `EC:1.2.1.16`

## Notes

Succinate semialdehyde dehydrogenase [NAD(P)+] Sad (SSADH) (SSDH) (EC 1.2.1.16)
