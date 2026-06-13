---
entity_id: "gene.b3410"
entity_type: "gene"
name: "feoC"
source_database: "NCBI RefSeq"
source_id: "gene-b3410"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3410"
  - "feoC"
---

# feoC

`gene.b3410`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3410`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

feoC (gene.b3410) is a gene entity. It encodes feoC (protein.P64638). Encoded protein function: FUNCTION: May function as a transcriptional regulator that controls feoABC expression. {ECO:0000255|HAMAP-Rule:MF_01586, ECO:0000269|PubMed:16718600}. EcoCyc product frame: EG12933-MONOMER. EcoCyc synonyms: yhgG. Genomic coordinates: 3542728-3542964. EcoCyc protein note: FeoC is part of a conserved ferrous iron transport system. Early studies in Escherichia coli K-12 strains characterized feo mutants which were defective in the import of ferrous iron . The feo operon consists of three co-regulated genes feoABC . FeoC may function as an [Fe-S] dependent transcriptional regulator of feo expression; the protein contains a predicted [Fe-S] cluster binding site and a LysR-like winged helix motif at its N-terminus . FeoC is required for full function of FeoB (Taudte, N., Diplomarbeit, cited in ). Anaerobically reconstituted FeoC contains a redox-active, ferredoxin-like [4Fe-4S]2+/+ cluster which is rapidly oxygen sensitive, degrading to a [2Fe-2S] cluster upon exposure to air . Cluster binding to FeoC leads to slight changes in protein conformation (although the protein remains monomeric) and FeoC may function as an oxygen-sensitive iron sensor . feo is a member of the Fur regulon; expression is repressed by Fur-Fe2+; feo expression is activated by FNR under anaerobic conditions...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by fnr (protein.P0A9E5), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64638|protein.P64638]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=feoC; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=feoC; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=feoC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011130,ECOCYC:EG12933,GeneID:947918`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3542728-3542964:+; feature_type=gene
