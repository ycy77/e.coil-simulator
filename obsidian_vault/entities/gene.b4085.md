---
entity_id: "gene.b4085"
entity_type: "gene"
name: "alsE"
source_database: "NCBI RefSeq"
source_id: "gene-b4085"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4085"
  - "alsE"
---

# alsE

`gene.b4085`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4085`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alsE (gene.b4085) is a gene entity. It encodes alsE (protein.P32719). Encoded protein function: FUNCTION: Catalyzes the reversible epimerization of D-allulose 6-phosphate to D-fructose 6-phosphate. Can also catalyze with lower efficiency the reversible epimerization of D-ribulose 5-phosphate to D-xylulose 5-phosphate. {ECO:0000255|HAMAP-Rule:MF_02226, ECO:0000269|PubMed:18700786, ECO:0000269|PubMed:9401019}. EcoCyc product frame: EG11957-MONOMER. EcoCyc synonyms: yjcU. Genomic coordinates: 4307783-4308478. EcoCyc protein note: Allulose-6-phosphate 3-epimerase catalyzes the final step in the degradation of D-allose, the conversion of D-allulose-6-phosphate to D-fructose-6-phosphate, which feeds into the glycolysis pathway . Crystal structures of AlsE have been solved. The enzyme has a (β/α)8 barrel structure; the active site is located at the C-terminal end of the β strands. Site-directed mutants that were predicted to alter substrate specificity have been purified and analyzed . Expression of alsE is induced by allose, and an alsE mutant is unable to catabolize allose . AlsE: "allulose 6-phosphate epimerase"

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32719|protein.P32719]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=alsE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013382,ECOCYC:EG11957,GeneID:948595`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4307783-4308478:-; feature_type=gene
