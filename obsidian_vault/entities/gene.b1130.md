---
entity_id: "gene.b1130"
entity_type: "gene"
name: "phoP"
source_database: "NCBI RefSeq"
source_id: "gene-b1130"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1130"
  - "phoP"
---

# phoP

`gene.b1130`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1130`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phoP (gene.b1130) is a gene entity. It encodes phoP (protein.P23836). Encoded protein function: FUNCTION: Member of the two-component regulatory system PhoP/PhoQ involved in adaptation to low Mg(2+) environments and the control of acid resistance genes. In low periplasmic Mg(2+), PhoQ phosphorylates PhoP, resulting in the expression of PhoP-activated genes (PAG) and repression of PhoP-repressed genes (PRG). In high periplasmic Mg(2+), PhoQ dephosphorylates phospho-PhoP, resulting in the repression of PAG and may lead to expression of some PRG (By similarity). Mediates magnesium influx to the cytosol by activation of MgtA. Promotes expression of the two-component regulatory system rstA/rstB and transcription of the hemL, mgrB, nagA, slyB, vboR and yrbL genes. {ECO:0000250, ECO:0000269|PubMed:10464230}. EcoCyc product frame: PHOSPHO-PHOP. Genomic coordinates: 1189776-1190447. EcoCyc protein note: PhoP is a dual transcriptional regulator that is activated in response to low extracellular levels of divalent cations, e.g., magnesium or calcium . In Escherichia coli K-12, PhoP activates transcription of a large collection of genes involved in Mg2+ homeostasis, resistance to antimicrobial peptides, acid resistance, and LPS modification . A mutation in the phoPQ genes generates cellular resistance to trimethoprim and nitrofurantoin under different growth conditions...

## Biological Role

Repressed by micA (gene.b4442), gcvB (gene.b4443), phoP (protein.P23836). Activated by rpoH (protein.P0AGB3), phoP (protein.P23836).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23836|protein.P23836]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=phoP; function=+
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=phoP; function=-+
- `represses` <-- [[gene.b4442|gene.b4442]] `RegulonDB` `S` - regulator=MicA; target=phoP; function=-
- `represses` <-- [[gene.b4443|gene.b4443]] `RegulonDB` `S` - regulator=GcvB; target=phoP; function=-
- `represses` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=phoP; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0003807,ECOCYC:EG10731,GeneID:945697`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1189776-1190447:-; feature_type=gene
