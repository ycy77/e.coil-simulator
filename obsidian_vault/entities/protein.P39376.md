---
entity_id: "protein.P39376"
entity_type: "protein"
name: "yjiE"
source_database: "UniProt"
source_id: "P39376"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjiE qseD b4327 JW4290"
---

# yjiE

`protein.P39376`

## Static

- Type: `protein`
- Source: `UniProt:P39376`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Protects cells from HOCl (hypochlorite) stress but not peroxide or diamide stress. Decreases the intracellular load of reactive oxygen species by up-regulating genes involved in methionine and cysteine biosynthesis and down-regulating Fur-regulated genes involved in iron acquisition. Has also been suggested to down-regulate expression of the flagellar regulon, decreasing motility, but this activity was not confirmed in a second study (PubMed:22223481). {ECO:0000269|PubMed:22223481}.

## Biological Role

Component of HypT-[Met]reduced (complex.ecocyc.CPLX0-7970), HypT-[Met-oxidized] DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-8075).

## Annotation

FUNCTION: Protects cells from HOCl (hypochlorite) stress but not peroxide or diamide stress. Decreases the intracellular load of reactive oxygen species by up-regulating genes involved in methionine and cysteine biosynthesis and down-regulating Fur-regulated genes involved in iron acquisition. Has also been suggested to down-regulate expression of the flagellar regulon, decreasing motility, but this activity was not confirmed in a second study (PubMed:22223481). {ECO:0000269|PubMed:22223481}.

## Outgoing Edges (7)

- `activates` --> [[gene.b0197|gene.b0197]] `RegulonDB` `S` - regulator=HypT; target=metQ; function=+
- `activates` --> [[gene.b0198|gene.b0198]] `RegulonDB` `S` - regulator=HypT; target=metI; function=+
- `activates` --> [[gene.b0199|gene.b0199]] `RegulonDB` `S` - regulator=HypT; target=metN; function=+
- `activates` --> [[gene.b0733|gene.b0733]] `RegulonDB` `S` - regulator=HypT; target=cydA; function=+
- `activates` --> [[gene.b0734|gene.b0734]] `RegulonDB` `S` - regulator=HypT; target=cydB; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7970|complex.ecocyc.CPLX0-7970]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8075|complex.ecocyc.CPLX0-8075]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4327|gene.b4327]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39376`
- `KEGG:ecj:JW4290;eco:b4327;ecoc:C3026_23390;`
- `GeneID:75202992;948852;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0042802`

## Notes

HTH-type transcriptional regulator YjiE (Hypochlorite-response regulator protein YjiE) (Quorum-sensing regulator protein D)
