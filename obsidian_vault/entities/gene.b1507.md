---
entity_id: "gene.b1507"
entity_type: "gene"
name: "hipA"
source_database: "NCBI RefSeq"
source_id: "gene-b1507"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1507"
  - "hipA"
---

# hipA

`gene.b1507`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1507`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hipA (gene.b1507) is a gene entity. It encodes hipA (protein.P23874). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system, first identified by mutations that increase production of persister cells, a fraction of cells that are phenotypic variants not killed by antibiotics, which lead to multidrug tolerance (PubMed:16707675, PubMed:26222023, PubMed:6348026, PubMed:8021189). Persistence may be ultimately due to global remodeling of the persister cell's ribosomes (PubMed:25425348). Phosphorylates Glu-tRNA-ligase (AC P04805, gltX, on 'Ser-239') in vivo (PubMed:24095282, PubMed:24343429). Phosphorylation of GltX prevents it from being charged, leading to an increase in uncharged tRNA(Glu). This induces amino acid starvation and the stringent response via RelA/SpoT and increased (p)ppGpp levels, which inhibits replication, transcription, translation and cell wall synthesis, reducing growth and leading to persistence and multidrug resistance (PubMed:24095282, PubMed:24343429). Once the level of HipA exceeds a threshold cells become dormant, and the length of dormancy is determined by how much HipA levels exceed the threshold (PubMed:20616060)...

## Biological Role

Repressed by hipB (protein.P23873). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23874|protein.P23874]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hipA; function=+
- `represses` <-- [[protein.P23873|protein.P23873]] `RegulonDB` `S` - regulator=HipB; target=hipA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005022,ECOCYC:EG10443,GeneID:946064`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1590854-1592176:-; feature_type=gene
