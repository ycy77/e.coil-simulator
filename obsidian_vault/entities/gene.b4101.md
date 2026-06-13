---
entity_id: "gene.b4101"
entity_type: "gene"
name: "phnG"
source_database: "NCBI RefSeq"
source_id: "gene-b4101"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4101"
  - "phnG"
---

# phnG

`gene.b4101`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4101`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnG (gene.b4101) is a gene entity. It encodes phnG (protein.P16685). Encoded protein function: FUNCTION: Together with PhnH, PhnI and PhnL is required for the transfer of the ribose triphosphate moiety from ATP to methyl phosphonate. {ECO:0000269|PubMed:22089136}. EcoCyc product frame: EG10716-MONOMER. Genomic coordinates: 4321244-4321696. EcoCyc protein note: PhnG, in a mixture together with PhnL, PhnH and PhnI, catalyzes the nucleophilic attack of CPD0-1068 on the anomeric carbon of ATP to form adenine and CPD0-2479 . PhnG was also found to be a component of a protein complex that was thought to function as a carbon-phosphorous lyase . phnG is part of an operon that is phosphate starvation-inducible and required for use of phosphonate and phosphite as phosphorous sources . PhnG appears to be required for carbon-phosphorous lyase activity . A phnG mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation .

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16685|protein.P16685]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnG; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013433,ECOCYC:EG10716,GeneID:948618`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4321244-4321696:-; feature_type=gene
