---
entity_id: "gene.b4100"
entity_type: "gene"
name: "phnH"
source_database: "NCBI RefSeq"
source_id: "gene-b4100"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4100"
  - "phnH"
---

# phnH

`gene.b4100`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4100`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnH (gene.b4100) is a gene entity. It encodes phnH (protein.P16686). Encoded protein function: FUNCTION: Together with PhnG, PhnI and PhnL is required for the transfer of the ribose triphosphate moiety from ATP to methyl phosphonate. {ECO:0000269|PubMed:22089136}. EcoCyc product frame: EG10717-MONOMER. Genomic coordinates: 4320663-4321247. EcoCyc protein note: PhnH, in a mixture together with PhnG, PhnL and PhnI, catalyzes the nucleophilic attack of CPD0-1068 on the anomeric carbon of ATP to form adenine and CPD0-2479 . PhnH was also found to be a component of a protein complex that was thought to function as a carbon-phosphorous lyase . phnH is part of an operon that is phosphate starvation-inducible and required for use of phosphonate and phosphite as phosphorous sources . PhnH is essential for C-P bond cleavage . A phnH mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation . A crystal structure of PhnH has been solved at 1.77 Å resolution. The purified protein is a dimer in solution .

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16686|protein.P16686]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnH; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013430,ECOCYC:EG10717,GeneID:948619`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4320663-4321247:-; feature_type=gene
