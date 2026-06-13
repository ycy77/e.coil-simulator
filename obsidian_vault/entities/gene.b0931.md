---
entity_id: "gene.b0931"
entity_type: "gene"
name: "pncB"
source_database: "NCBI RefSeq"
source_id: "gene-b0931"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0931"
  - "pncB"
---

# pncB

`gene.b0931`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0931`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pncB (gene.b0931) is a gene entity. It encodes pncB (protein.P18133). Encoded protein function: FUNCTION: Catalyzes the synthesis of beta-nicotinate D-ribonucleotide from nicotinate and 5-phospho-D-ribose 1-phosphate at the expense of ATP. {ECO:0000255|HAMAP-Rule:MF_00570, ECO:0000269|PubMed:2211655}. EcoCyc product frame: NICOTINATEPRIBOSYLTRANS-MONOMER. Genomic coordinates: 989154-990356. EcoCyc protein note: Nicotinate phosphoribosyltransferase (NAPRTase) mediates the formation of nicotinate mononucleotide from exogenous nicotinate and PRPP. The product is then converted intracellularly into NAD . NAPRTase appears to be the rate-limiting enzyme in the biosynthesis of NAD from nicotinate . NAPRTase levels decrease in response to added extracellular nicotinate. Overexpression of pncB increases the intracellular level of NAD . NAPRTase was reported to localize to the periplasm . However, the enzyme does not have a recognizable signal sequence, and N-terminal sequencing of the partially purified protein gives no indication of N-terminal processing of the enzyme. Additional unpublished evidence for localization to the periplasm or cytoplasmic membrane is mentioned . pncB shows differential codon adaptation, resulting in differential translation efficiency signatures, in thermophilic microbes. It was therefore predicted to play a role in the heat shock response...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18133|protein.P18133]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pncB; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=pncB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003167,ECOCYC:EG10742,GeneID:946648`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:989154-990356:-; feature_type=gene
