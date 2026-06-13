---
entity_id: "gene.b4705"
entity_type: "gene"
name: "mntS"
source_database: "NCBI RefSeq"
source_id: "gene-b4705"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4705"
  - "mntS"
---

# mntS

`gene.b4705`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4705`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mntS (gene.b4705) is a gene entity. It encodes mntS (protein.P0DKB3). Encoded protein function: FUNCTION: Small protein involved in manganese homeostasis (PubMed:21908668, PubMed:25774656, PubMed:38104967). Inhibits the manganese exporter MntP when manganese levels drop (PubMed:25774656, PubMed:38104967). Acts by binding directly to MntP, preventing its manganese export activity (PubMed:38104967). Under steady-state low manganese levels, may facilitate manganese delivery to manganese-dependent enzymes (PubMed:25774656). Required for repression of mntH by MntR (PubMed:21908668). {ECO:0000269|PubMed:21908668, ECO:0000269|PubMed:25774656, ECO:0000269|PubMed:38104967}. EcoCyc product frame: MONOMER0-4216. EcoCyc synonyms: G0-8881. Genomic coordinates: 852869-852997. EcoCyc protein note: MntS is a small protein that affects the availability of Mn2+ within the cell . Synthesis of MntS increases the total intracellular levels of Mn2+, likely by directly or indirectly inhibiting manganese export through G6999-MONOMER MntP. Under Mn2+-limiting conditions, MntS confers resistance to hydrogen peroxide by facilitating delivery of Mn2+ to Mn2+-dependent enzymes . Expression of mntS is high during exponential growth in minimal media and is repressed by MntR in response to Mn2+...

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), rpoD (protein.P00579), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DKB3|protein.P0DKB3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mntS; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=mntS; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10715,GeneID:14678509`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:852869-852997:-; feature_type=gene
