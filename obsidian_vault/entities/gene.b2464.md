---
entity_id: "gene.b2464"
entity_type: "gene"
name: "talA"
source_database: "NCBI RefSeq"
source_id: "gene-b2464"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2464"
  - "talA"
---

# talA

`gene.b2464`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2464`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

talA (gene.b2464) is a gene entity. It encodes talA (protein.P0A867). Encoded protein function: FUNCTION: Transaldolase is important for the balance of metabolites in the pentose-phosphate pathway. EcoCyc product frame: TRANSALDOLA-MONOMER. Genomic coordinates: 2578666-2579616. EcoCyc protein note: Transaldolase is an enzyme of the pentose phosphate pathway, where it catalyzes the reversible interconversion of glyceraldehyde-3-phosphate and sedoheptulose-7-phosphate to fructose-6-phosphate and erythrose-4-phosphate. The reversibility of this reaction and carbon flux through the pentose phosphate pathway has been addressed both experimentally (summarized in ) and theoretically . There are two closely related transaldolases in E. coli, encoded by talA and talB. Transaldolase A has not been biochemically characterized. Under aerobic growth conditions with glucose as the sole source of carbon, a talA mutant shows a similar growth rate, but a decreased acetate production and increased biomass yield compared to wild type . A talA mutant is more sensitive to gentamicin than wild-type . Protein levels of TalA are induced by osmotic stress only under aerobic conditions and by exposure to mercury . talA belongs to the σS regulon ; its expression increases in early stationary phase just as expression of talB decreases...

## Biological Role

Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A867|protein.P0A867]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=talA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008115,ECOCYC:EG11797,GeneID:947006`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2578666-2579616:+; feature_type=gene
