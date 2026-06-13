---
entity_id: "gene.b3613"
entity_type: "gene"
name: "envC"
source_database: "NCBI RefSeq"
source_id: "gene-b3613"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3613"
  - "envC"
---

# envC

`gene.b3613`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3613`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

envC (gene.b3613) is a gene entity. It encodes envC (protein.P37690). Encoded protein function: FUNCTION: Activator of the cell wall hydrolases AmiA and AmiB. Required for septal murein cleavage and daughter cell separation during cell division. In vitro, exhibits weak endoproteolytic activity on beta-casein. {ECO:0000269|PubMed:11976287, ECO:0000269|PubMed:15165230, ECO:0000269|PubMed:19525345, ECO:0000269|PubMed:20300061, ECO:0000269|PubMed:23796240}. EcoCyc product frame: EG12297-MONOMER. EcoCyc synonyms: yibP, slm11. Genomic coordinates: 3786838-3788097. EcoCyc protein note: EnvC is a divisome associated factor which activates the peptidoglycan (PG) hydrolases NACMURLALAAMI1-MONOMER "AmiA" and NACMURLALAAMI2-MONOMER "AmiB" required for septal splitting . EnvC-mediated amidase activation is regulated by direct interaction with the ABC-54-CPLX FtsEX transmembrane complex (reviewed in ). EnvC contains a structural element - the 'restraining arm' - that is implicated in a self-inhibition mechanism; FtsEX interaction with EnvC may drive conformational change that leads to amidase activation (see further ). EnvC is not essential for viability; an envC null mutant has cell division and cell envelope integrity defects, an FtsZ ring defect, and is unable to form colonies at 42oC . Temperature sensitivity can be rescued by addition of 5% betaine to the medium...

## Biological Role

Repressed by cra (protein.P0ACP1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37690|protein.P37690]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=envC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011820,ECOCYC:EG12297,GeneID:948129`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3786838-3788097:+; feature_type=gene
