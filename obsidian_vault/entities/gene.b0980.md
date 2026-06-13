---
entity_id: "gene.b0980"
entity_type: "gene"
name: "appA"
source_database: "NCBI RefSeq"
source_id: "gene-b0980"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0980"
  - "appA"
---

# appA

`gene.b0980`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0980`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

appA (gene.b0980) is a gene entity. It encodes appA (protein.P07102). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of phytate (or myo-inositol hexakisphosphate, an indigestible organic form of phosphorus that is found in many plant tissues) to myo-inositol and inorganic phosphate (PubMed:10696472, PubMed:11035187, PubMed:30712472, PubMed:8387749, Ref.8). Dephosphorylates phytate in a stereospecific way by sequential removal of phosphate groups to produce myo-inositol 2-monophosphate (PubMed:11035187). Also shows phosphoanhydride phosphatase activity and hydrolyzes the distal phosphoryl residues of GTP, the 5'-beta-phosphoryl residue of the regulatory nucleotide ppGpp and tripolyphosphates (PubMed:1429631, PubMed:6282821, PubMed:8407904). Does not split most phosphomonoesters with the exception of the synthetic substrate p-nitrophenyl phosphate (pNPP), 2,3-bisphosphoglycerate and fructose 1,6-bisphosphate (PubMed:10696472, PubMed:1429631, PubMed:6282821, PubMed:8387749, PubMed:8407904, Ref.8). {ECO:0000269|PubMed:10696472, ECO:0000269|PubMed:11035187, ECO:0000269|PubMed:1429631, ECO:0000269|PubMed:30712472, ECO:0000269|PubMed:6282821, ECO:0000269|PubMed:8387749, ECO:0000269|PubMed:8407904, ECO:0000269|Ref.8}. EcoCyc product frame: APPA-MONOMER. Genomic coordinates: 1040617-1041915...

## Biological Role

Activated by ydeO (protein.P76135).

## Enriched Pathways

- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07102|protein.P07102]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=appA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003305,ECOCYC:EG10049,GeneID:946206`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1040617-1041915:+; feature_type=gene
