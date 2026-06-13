---
entity_id: "gene.b0591"
entity_type: "gene"
name: "entS"
source_database: "NCBI RefSeq"
source_id: "gene-b0591"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0591"
  - "entS"
---

# entS

`gene.b0591`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0591`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

entS (gene.b0591) is a gene entity. It encodes entS (protein.P24077). Encoded protein function: FUNCTION: Component of an export pathway for enterobactin (PubMed:12068807). Overexpression reduces intracellular arabinose concentrations (PubMed:22952739). {ECO:0000269|PubMed:12068807, ECO:0000269|PubMed:22952739}. EcoCyc product frame: YBDA-MONOMER. EcoCyc synonyms: ybdA. Genomic coordinates: 622300-623550. EcoCyc protein note: The EntS protein is a member of the major facilitator superfamily (MFS) of transporters . Based on sequence similarity, it functions as a proton-driven efflux system. Siderophore nutrition assays have shown that an entS mutant is unable to export enterobactin efficiently to alleviate iron deprivation , though some export does still occur through another mechanism. entS was identified in a screen for genes that reduce the lethal effects of stress; an entS insertion mutant is more sensitive than wild type to mitomycin C and other stresses . EntS has been implicated in arabinose efflux .

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24077|protein.P24077]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=entS; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=entS; function=-+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=entS; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002036,ECOCYC:EG11104,GeneID:946268`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:622300-623550:+; feature_type=gene
