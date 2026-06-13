---
entity_id: "gene.b2500"
entity_type: "gene"
name: "purN"
source_database: "NCBI RefSeq"
source_id: "gene-b2500"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2500"
  - "purN"
---

# purN

`gene.b2500`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2500`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purN (gene.b2500) is a gene entity. It encodes purN (protein.P08179). Encoded protein function: FUNCTION: Catalyzes the transfer of a formyl group from 10-formyltetrahydrofolate to 5-phospho-ribosyl-glycinamide (GAR), producing 5-phospho-ribosyl-N-formylglycinamide (FGAR) and tetrahydrofolate. {ECO:0000255|HAMAP-Rule:MF_01930, ECO:0000269|PubMed:2185839, ECO:0000269|PubMed:350869}. EcoCyc product frame: GART-MONOMER. EcoCyc synonyms: ade(c), ade. Genomic coordinates: 2622234-2622872. EcoCyc protein note: E. coli contains two different phosphoribosylglycinamide (GAR) transformylases, both of which can catalyze the third step in de novo purine biosynthesis. The transformylase encoded by purN utilizes 10-formyl-tetrahydrofolate as the formyl donor. The second transformylase encoded by purT utilizes formate, which is provided by PurU-catalyzed hydrolysis of 10-formyl-tetrahydrofolate . The existence of these two transformylase enzymes was determined by mutant studies. A strain containing a knockout insertion in purN did not result in purine auxotrophy . Only mutants defective in both purN and purT required exogenously added purine for growth . There is no significant homology between the two transformylases . In early work using E. coli B, 10-formyltetrahydrofolate was identified as the formyl donor for this enzyme . Later work using E...

## Biological Role

Repressed by fnr (protein.P0A9E5), purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08179|protein.P08179]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=purN; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=purN; function=-
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=purN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008232,ECOCYC:EG10799,GeneID:946973`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2622234-2622872:+; feature_type=gene
