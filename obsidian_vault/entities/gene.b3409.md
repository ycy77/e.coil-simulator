---
entity_id: "gene.b3409"
entity_type: "gene"
name: "feoB"
source_database: "NCBI RefSeq"
source_id: "gene-b3409"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3409"
  - "feoB"
---

# feoB

`gene.b3409`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3409`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

feoB (gene.b3409) is a gene entity. It encodes feoB (protein.P33650). Encoded protein function: FUNCTION: Transporter of a GTP-driven Fe(2+) uptake system, probably couples GTP-binding to channel opening and Fe(2+) uptake (PubMed:12446835, PubMed:19629046). A guanine nucleotide-binding protein (G proteins) in which the guanine nucleotide binding site alternates between an active, GTP-bound state and an inactive, GDP-bound state. This protein has fast intrinsic GDP release, mediated by the G5 loop (about residues 149-158). Presumably GTP hydrolysis leads to conformational changes and channel closing (PubMed:19629046). A GDP release mechanism involving a conformational change of the G5 loop (and thus the removal of the nucleotide-binding and stabilizing interactions) would significantly reduce the affinity for GDP, and conceivably be sufficient for catalysing nucleotide release (PubMed:25374115). {ECO:0000269|PubMed:12446835, ECO:0000269|PubMed:19629046, ECO:0000269|PubMed:23104801, ECO:0000269|PubMed:25374115, ECO:0000269|PubMed:25517170, ECO:0000269|PubMed:8407793}. EcoCyc product frame: FEOB-MONOMER. Genomic coordinates: 3540407-3542728. EcoCyc protein note: FeoB is the inner membrane component of a ferrous iron uptake system which is active under anaerobic growth conditions...

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by fnr (protein.P0A9E5), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33650|protein.P33650]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=feoB; function=+
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `C` - regulator=OmpR; target=feoB; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=feoB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011126,ECOCYC:EG12102,GeneID:947919`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3540407-3542728:+; feature_type=gene
