---
entity_id: "gene.b0194"
entity_type: "gene"
name: "proS"
source_database: "NCBI RefSeq"
source_id: "gene-b0194"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0194"
  - "proS"
---

# proS

`gene.b0194`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0194`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proS (gene.b0194) is a gene entity. It encodes proS (protein.P16659). Encoded protein function: FUNCTION: Catalyzes the attachment of proline to tRNA(Pro) in a two-step reaction: proline is first activated by ATP to form Pro-AMP and then transferred to the acceptor end of tRNA(Pro). As ProRS can inadvertently accommodate and process non-cognate amino acids such as alanine and cysteine, to avoid such errors it has two additional distinct editing activities against alanine. One activity is designated as 'pretransfer' editing and involves the tRNA(Pro)-independent hydrolysis of activated Ala-AMP. The other activity is designated 'posttransfer' editing and involves deacylation of mischarged Ala-tRNA(Pro). Misacylated Cys-tRNA(Pro) is not edited by ProRS, but instead may be edited in trans by YbaK. EcoCyc product frame: PROS-MONOMER. EcoCyc synonyms: drp, drpA. Genomic coordinates: 217057-218775. EcoCyc protein note: Proline-tRNA ligase (ProRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. ProRS belongs to the Class IIA aminoacyl-tRNA synthetases . ProRS of E. coli B is a dimer in solution . Specificity determinants within tRNAPro that are important for recognition by ProRS have been identified...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16659|protein.P16659]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=proS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000657,ECOCYC:EG10770,GeneID:949116`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:217057-218775:-; feature_type=gene
