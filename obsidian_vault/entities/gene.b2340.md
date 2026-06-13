---
entity_id: "gene.b2340"
entity_type: "gene"
name: "sixA"
source_database: "NCBI RefSeq"
source_id: "gene-b2340"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2340"
  - "sixA"
---

# sixA

`gene.b2340`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2340`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sixA (gene.b2340) is a gene entity. It encodes sixA (protein.P76502). Encoded protein function: FUNCTION: Exhibits phosphohistidine phosphatase activity towards the HPt domain of the ArcB sensor involved in the multistep His-Asp phosphorelay. EcoCyc product frame: G7211-MONOMER. EcoCyc synonyms: yfcW. Genomic coordinates: 2456327-2456812. EcoCyc protein note: SixA is a phosphohistidine phosphatase. Genetic evidence suggested that MONOMER0-4292 NPr-P is a target for dephosphorylation by SixA ; the activity has now been confirmed in vitro . Dephosphorylation of NPr-P by SixA involves formation of a transient phosphohistidine intermediate . SixA was shown to remove the phosphoryl group from the His717 residue of PHOSPHO-ARCB717 ArcB in vitro . Initial results showed that under anaerobic growth conditions, dephosphorylation of ArcB accelerates the derepression of the sdh operon via the ArcB/ArcA phosphorelay in the presence of anaerobic electron acceptors . However, a later report shows no evidence that SixA affects ArcB/ArcA signaling to icdA expression under anaerobic conditions in vivo . SixA dephosphorylates the inactive, phosphorylated 6PFK-1-MONOMER reversing its inhibition . Crystal structures of the free and tungstate-bound forms of SixA have been solved at 2.06 and 1.9 Å resolution...

## Biological Role

Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76502|protein.P76502]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sixA; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=sixA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007720,ECOCYC:G7211,GeneID:946815`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2456327-2456812:-; feature_type=gene
