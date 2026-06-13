---
entity_id: "gene.b1308"
entity_type: "gene"
name: "pspE"
source_database: "NCBI RefSeq"
source_id: "gene-b1308"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1308"
  - "pspE"
---

# pspE

`gene.b1308`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1308`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pspE (gene.b1308) is a gene entity. It encodes pspE (protein.P23857). Encoded protein function: FUNCTION: The phage shock protein (psp) operon (pspABCDE) may play a significant role in the competition for survival under nutrient- or energy-limited conditions. PspE catalyzes the sulfur-transfer reaction from thiosulfate to cyanide, to form sulfite and thiocyanate. Also able to use dithiol (dithiothreitol) as an alternate sulfur acceptor. Also possesses a very low mercaptopyruvate sulfurtransferase activity. EcoCyc product frame: EG10780-MONOMER. Genomic coordinates: 1369689-1370003. EcoCyc protein note: PspE is a periplasmic sulfurtransferase of the rhodanese family that catalyzes the transfer of sulfur from S2O3 to a recipient thiol compound . Based on analysis of deletion mutants, PspE appears to carry out about 85% of the thiosulfate sulfurtransferase activity, with CPLX0-242 "GlpE" accounting for approximately 10% . The main receipient of the sulfur is GLUTATHIONE (GSH), the dominant cellular thiol in E. coli . The product, CPD-11281 (GSSH), was shown to be the dominant species of cellular sulfane sulfur. It should be noted that the reaction is strongly inhibited by GSSH, and thus the reaction normally favors the reverse direction. The forward reaction is enhanced by the removal of GSSH via translocation from the periplasm to the cytoplasm...

## Biological Role

Activated by pspF (protein.P37344).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23857|protein.P23857]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37344|protein.P37344]] `RegulonDB` `S` - regulator=PspF; target=pspE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004397,ECOCYC:EG10780,GeneID:945652`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1369689-1370003:+; feature_type=gene
