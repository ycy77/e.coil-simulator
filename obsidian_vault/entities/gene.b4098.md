---
entity_id: "gene.b4098"
entity_type: "gene"
name: "phnJ"
source_database: "NCBI RefSeq"
source_id: "gene-b4098"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4098"
  - "phnJ"
---

# phnJ

`gene.b4098`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4098`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnJ (gene.b4098) is a gene entity. It encodes phnJ (protein.P16688). Encoded protein function: FUNCTION: Catalyzes the breakage of the C-P bond in alpha-D-ribose 1-methylphosphonate 5-phosphate (PRPn) forming alpha-D-ribose 1,2-cyclic phosphate 5-phosphate (PRcP). {ECO:0000269|PubMed:22089136}. EcoCyc product frame: EG10719-MONOMER. Genomic coordinates: 4318761-4319606. EcoCyc protein note: PhnJ is a radical SAM enzyme that catalyzes the cleavage of CPD0-2480 (PRPn) to CPD0-2463 (PRcP). Activity requires anaerobic reconstitution of a [4Fe-4S] cluster and the presence of dithionite . PhnJ was also found to be a component of a protein complex that was thought to catalyze the carbon-phosphorus lyase reaction . phnJ is part of an operon that is phosphate starvation-inducible and required for use of phosphonate and phosphite as phosphorous sources . PhnJ appears to be required for carbon-phosphorous lyase activity . A phnJ mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation .

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16688|protein.P16688]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnJ; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnJ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013426,ECOCYC:EG10719,GeneID:948606`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4318761-4319606:-; feature_type=gene
