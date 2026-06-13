---
entity_id: "gene.b0313"
entity_type: "gene"
name: "betI"
source_database: "NCBI RefSeq"
source_id: "gene-b0313"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0313"
  - "betI"
---

# betI

`gene.b0313`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0313`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

betI (gene.b0313) is a gene entity. It encodes betI (protein.P17446). Encoded protein function: FUNCTION: Repressor involved in the biosynthesis of the osmoprotectant glycine betaine. It represses transcription of the choline transporter BetT and the genes of BetAB involved in the synthesis of glycine betaine. {ECO:0000269|PubMed:8626294, ECO:0000269|PubMed:8626295}. EcoCyc product frame: PD00251. Genomic coordinates: 328747-329334. EcoCyc protein note: "Betaine inhibitor," BetI, acts as a repressor of glycine betaine synthesis from choline . It is negatively autoregulated and coordinately represses transcription of the choline transporter and the operon related to the synthesis of glycine betaine. These divergent operons are expressed only under aerobic conditions and are induced by osmotic stress . BetI is an unusual repressor because it remains bound to DNA during induction. BetI forms a complex with DNA in the presence of choline, binding to a 20-bp-long sequence with dyad symmetry that overlaps betTp and betIp simultaneously . The position of the repressor gene within the operon is unusual too, as regulatory genes tend to be positioned at the end of operons and this gene is located at the beginning of the operon. BetI is still able to repress transcription at positions as far as -61 from the TSS, but in a weak manner...

## Biological Role

Repressed by betI (protein.P17446).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17446|protein.P17446]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P17446|protein.P17446]] `RegulonDB` `C` - regulator=BetI; target=betI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001076,ECOCYC:EG10111,GeneID:944981`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:328747-329334:-; feature_type=gene
