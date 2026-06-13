---
entity_id: "gene.b4102"
entity_type: "gene"
name: "phnF"
source_database: "NCBI RefSeq"
source_id: "gene-b4102"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4102"
  - "phnF"
---

# phnF

`gene.b4102`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4102`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnF (gene.b4102) is a gene entity. It encodes phnF (protein.P16684). Encoded protein function: FUNCTION: Belongs to an operon involved in alkylphosphonate uptake and C-P lyase. Exact function not known. By similarity could be a transcriptional regulator. EcoCyc product frame: EG10715-MONOMER. Genomic coordinates: 4321697-4322422. EcoCyc protein note: PhnF is a predicted transcriptional regulator that belongs to the HutC subfamily of the GntR family of transcriptional regulators. It consists of two domains, an amino-terminal domain that contains a potential helix-turn-helix DNA-binding motif and a carboxy-terminal domain involved in effector recognition . A crystal structure of the C-terminal domain of PhnF has been solved at 1.7 Å resolution . A non-polar phnF mutation has no effect on the ability to utilize phosphonates as the source of phosphate . A phnF mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation .

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16684|protein.P16684]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnF; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013435,ECOCYC:EG10715,GeneID:948617`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4321697-4322422:-; feature_type=gene
