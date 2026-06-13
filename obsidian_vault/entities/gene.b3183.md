---
entity_id: "gene.b3183"
entity_type: "gene"
name: "obgE"
source_database: "NCBI RefSeq"
source_id: "gene-b3183"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3183"
  - "obgE"
---

# obgE

`gene.b3183`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3183`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

obgE (gene.b3183) is a gene entity. It encodes obgE (protein.P42641). Encoded protein function: FUNCTION: An essential GTPase which binds GTP, GDP and possibly (p)ppGpp with moderate affinity, with high nucleotide exchange rates and a fairly low GTP hydrolysis rate. Plays a role in control of the cell cycle, stress response, ribosome biogenesis and in those bacteria that undergo differentiation, in morphogenesis control. {ECO:0000255|HAMAP-Rule:MF_01454}.; FUNCTION: Required for chromosome segregation (PubMed:11555285). Plays a role in the stringent response, perhaps by sequestering 50S ribosomal subunits and decreasing protein synthesis (PubMed:19555460). Has a non-essential role in the late steps of ribosome biogenesis, coordinating 50S ribosomal subunit assembly (PubMed:24844575, PubMed:33639093). Has high guanosine nucleotide exchange rate constants for GTP and GDP, and a relatively low GTP hydrolysis rate stimulated by the 50S ribosomal subunit. It is estimated there are 34000 molecules in log-phase cells and 5600 molecules in stationary-phase cells. Overexpression increases bacterial persistence (in exponential and stationary phase) in response to antibiotics (PubMed:26051177)...

## Biological Role

Activated by rpoD (protein.P00579), mlrA (protein.P33358).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P42641|protein.P42641]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=obgE; function=+
- `activates` <-- [[protein.P33358|protein.P33358]] `RegulonDB` `S` - regulator=MlrA; target=obgE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010462,ECOCYC:G7656,GeneID:947694`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3330582-3331754:-; feature_type=gene
