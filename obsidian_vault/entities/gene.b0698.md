---
entity_id: "gene.b0698"
entity_type: "gene"
name: "kdpA"
source_database: "NCBI RefSeq"
source_id: "gene-b0698"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0698"
  - "kdpA"
---

# kdpA

`gene.b0698`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0698`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdpA (gene.b0698) is a gene entity. It encodes kdpA (protein.P03959). Encoded protein function: FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894, PubMed:2849541, PubMed:8499455). This subunit binds the periplasmic potassium ions and delivers the ions to the membrane domain of KdpB through an intramembrane tunnel (PubMed:30478378, PubMed:34272288, PubMed:7896809). {ECO:0000269|PubMed:23930894, ECO:0000269|PubMed:2849541, ECO:0000269|PubMed:30478378, ECO:0000269|PubMed:34272288, ECO:0000269|PubMed:7896809, ECO:0000269|PubMed:8499455}. EcoCyc product frame: EG10513-MONOMER. EcoCyc synonyms: kac. Genomic coordinates: 727059-728732. EcoCyc protein note: KdpA is an innner membrane subunit of the potassium ion importing Kdp ATPase ; KdpA contains 12 predicted transmembrane regions and forms the K+ transporting channel of the complex; both periplasmic and cytoplasmic K+ binding sites have been identified . More recently, cryo-EM structures of the KdpFABC complex suggest a translocation pathway for K+ via KdpA and KdpB half-channels (and further ). KdpA contains 4 M1-P-M2 (MPM) transmembrane motifs and may be homologous to the transmembrane subunits of K+ symporters...

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), kdpE (protein.P21866).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03959|protein.P03959]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kdpA; function=+
- `activates` <-- [[protein.P21866|protein.P21866]] `RegulonDB` `C` - regulator=KdpE; target=kdpA; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=kdpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002381,ECOCYC:EG10513,GeneID:946045`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:727059-728732:-; feature_type=gene
