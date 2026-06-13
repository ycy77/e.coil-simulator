---
entity_id: "gene.b0314"
entity_type: "gene"
name: "betT"
source_database: "NCBI RefSeq"
source_id: "gene-b0314"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0314"
  - "betT"
---

# betT

`gene.b0314`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0314`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

betT (gene.b0314) is a gene entity. It encodes betT (protein.P0ABC9). Encoded protein function: FUNCTION: High-affinity uptake of choline driven by a proton-motive force. {ECO:0000269|PubMed:1956285}. EcoCyc product frame: BETT-MONOMER. Genomic coordinates: 329463-331496. EcoCyc protein note: BetT is a proton-motive-force-driven choline transporter that belongs to the Betaine Carnitine Choline Transport (BCCT) family of proteins. Deletion mutants of betT displayed essentially no choline uptake activity, but could be complemented with a betT-encoding plasmid, restoring rapid choline uptake . Choline uptake is completely inhibited by the protonophore carbonylcyanide p-trifluoromethoxyphenyl hydrazone, suggesting that choline transport by BetT is driven by the proton-motive force . Choline is used to synthesize glycine betaine, which is used by E. coli to overcome growth inhibition caused by osmotic stress . The betTIAB genes are expressed only under aerobic conditions, and are induced by osmotic stress . Analysis of betT-lacZ fusions showed that betT transcription increased 7-10 fold in response to increases in medium osmolarity. The presence of choline further increases this response . betT mRNA decay is controlled by RNase III in response to osmotic stress. betT mRNA contains two tandem RNase III cleavage sites - both of which are required for efficient betT mRNA degradation...

## Biological Role

Repressed by arcA (protein.P0A9Q1), betI (protein.P17446).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABC9|protein.P0ABC9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=betT; function=-
- `represses` <-- [[protein.P17446|protein.P17446]] `RegulonDB` `C` - regulator=BetI; target=betT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001080,ECOCYC:EG10112,GeneID:945079`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:329463-331496:+; feature_type=gene
