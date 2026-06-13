---
entity_id: "gene.b0529"
entity_type: "gene"
name: "folD"
source_database: "NCBI RefSeq"
source_id: "gene-b0529"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0529"
  - "folD"
---

# folD

`gene.b0529`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0529`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

folD (gene.b0529) is a gene entity. It encodes folD (protein.P24186). Encoded protein function: FUNCTION: Catalyzes the oxidation of 5,10-methylenetetrahydrofolate to 5,10-methenyltetrahydrofolate and then the hydrolysis of 5,10-methenyltetrahydrofolate to 10-formyltetrahydrofolate. This enzyme is specific for NADP. {ECO:0000255|HAMAP-Rule:MF_01576, ECO:0000269|PubMed:1748668}. EcoCyc product frame: FOLD-MONOMER. EcoCyc synonyms: ads. Genomic coordinates: 556875-557741. EcoCyc protein note: The folD gene product is a bifunctional enzyme that catalyzes the NADP+-dependent dehydrogenation of N5,N10-methylenetetrahydrofolate and the subsequent cyclohydrolysis reaction that generates N10-formyltetrahydrofolate . N10-formyltetrahydrofolates are involved in tetrahydrofolate and purine biosynthesis and supply the formyl group for the initiator tRNAfMet. The macrolide carboxylate carolacton inhibits both activities of FolD; mutant enzymes that confer resistance to carolacton have been isolated . Crystal structures of FolD and the FolD-carolacton complex have been solved . Each monomer comprises two domains that form an interdomain cleft. The homodimeric form appears to be stabilized by an intersubunit disulfide bond between the Cys132 residues of each subunit...

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24186|protein.P24186]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001818,ECOCYC:EG10328,GeneID:945221`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:556875-557741:-; feature_type=gene
