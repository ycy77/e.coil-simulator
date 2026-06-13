---
entity_id: "gene.b1740"
entity_type: "gene"
name: "nadE"
source_database: "NCBI RefSeq"
source_id: "gene-b1740"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1740"
  - "nadE"
---

# nadE

`gene.b1740`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1740`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nadE (gene.b1740) is a gene entity. It encodes nadE (protein.P18843). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent amidation of deamido-NAD to form NAD. Uses ammonia as a nitrogen source. {ECO:0000255|HAMAP-Rule:MF_00193, ECO:0000269|PubMed:8195100}. EcoCyc product frame: NAD-SYNTH-MONOMER. EcoCyc synonyms: efg, ntrL. Genomic coordinates: 1822458-1823285. EcoCyc protein note: NAD+ synthetase is an essential enzyme involved in both the de novo biosynthesis and salvage of NAD+, catalyzing the final step of both pathways. The enzyme shows a strong preference for ammonia over glutamine as the amino group donor and may even have no glutamine-dependent NAD+ synthetase activity at all . The enzyme contains a P-loop-like pyrophosphatase motif . Crystal structures of the enzyme alone and in complex with substrates and the reaction product NAD+ have been solved. The catalytic cycle appears to involve significant structural reorganization . nadE is essential for growth . In the presence of a heterologous NAD+ transporter, a ΔnadE mutant is able to grow with externally supplied NAD+ . Expression of nadE is posttranscriptionally regulated by the small RNA CyaR . Efg: "essential for growth" NadE: "NAD biosynthesis E" Reviews:

## Biological Role

Repressed by cyaR (gene.b4438). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18843|protein.P18843]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nadE; function=+
- `represses` <-- [[gene.b4438|gene.b4438]] `RegulonDB` `S` - regulator=CyaR; target=nadE; function=-

## External IDs

- `Dbxref:ECOCYC:EG10663,GeneID:946946`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1822458-1823285:+; feature_type=gene
