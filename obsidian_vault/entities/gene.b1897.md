---
entity_id: "gene.b1897"
entity_type: "gene"
name: "otsB"
source_database: "NCBI RefSeq"
source_id: "gene-b1897"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1897"
  - "otsB"
---

# otsB

`gene.b1897`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1897`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

otsB (gene.b1897) is a gene entity. It encodes otsB (protein.P31678). Encoded protein function: FUNCTION: Removes the phosphate from trehalose 6-phosphate (Tre6P) to produce free trehalose. Also catalyzes the dephosphorylation of glucose-6-phosphate (Glu6P) and 2-deoxyglucose-6-phosphate (2dGlu6P). {ECO:0000269|PubMed:1310094, ECO:0000269|PubMed:16990279}. EcoCyc product frame: TREHALOSEPHOSPHASYN-MONOMER. EcoCyc synonyms: otsP. Genomic coordinates: 1981587-1982387. EcoCyc protein note: otsB encodes the biosynthetic trehalose-6-phosphate phosphatase, which belongs to the superfamily of haloacid dehalogenase (HAD)-like hydrolases . The phosphatase activity of OtsB was also found in a high-throughput screen of purified proteins . Accumulation of trehalose at low temperatures enhances cell viability . An otsBA double mutant is more sensitive than wild type to heat shock during stationary phase, but not during exponential growth . Expression of otsB is increased under osmotic stress and induced during the transition to stationary phase and by low temperature in a σS-dependent manner . Stability of otsBA mRNA is increased approximately 10-fold at 16°C compared to 37°C . Under nutrient-limiting conditions in an RpoS mutant strain background, an adaptive mutation that allows RpoS-independent transcription of otsBA arises spontaneously and increases fitness...

## Biological Role

Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31678|protein.P31678]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=otsB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006320,ECOCYC:EG11752,GeneID:946406`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1981587-1982387:-; feature_type=gene
