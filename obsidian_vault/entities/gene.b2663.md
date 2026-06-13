---
entity_id: "gene.b2663"
entity_type: "gene"
name: "gabP"
source_database: "NCBI RefSeq"
source_id: "gene-b2663"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2663"
  - "gabP"
---

# gabP

`gene.b2663`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2663`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gabP (gene.b2663) is a gene entity. It encodes gabP (protein.P25527). Encoded protein function: FUNCTION: Transporter for gamma-aminobutyrate (GABA) (PubMed:8297211, PubMed:8557687). Transport is driven by the membrane potential (PubMed:8297211). Can also transport a number of GABA analogs such as nipecotic acid or muscimol (PubMed:8557687). {ECO:0000269|PubMed:8297211, ECO:0000269|PubMed:8557687}. EcoCyc product frame: GABP-MONOMER. Genomic coordinates: 2794253-2795653. EcoCyc protein note: GabP mediates the uptake of 4-aminobutanoate, the zwitterionic form of γ-aminobutyric acid (GABA). gabP encodes a predicted integral membrane protein; moderate overexpression of cloned gabP enhances uptake of labeled GABA; GabP is a high affinity GABA transporter that is driven by membrane potential . Both open chain and cyclic analogs of GABA (eg. 5-aminopentanoate, piperidine-3-carboxylate) are effective inhibitors of GABA transport ; GabP transports a range of structurally diverse GABA analogs . Experimental topology analysis suggests the protein contains 12 transmembrane domains with the N and C-termini located in the cytoplasm . GabP mediated transport of GABA is dependent upon the presence of phosphatidylethanolamine (PE) within the membrane; in cells lacking PE, the N-terminal hairpin domain of GabP is misorganized and transport function is compromised...

## Biological Role

Repressed by glaR (protein.P37338). Activated by lrp (protein.P0ACJ0), crp (protein.P0ACJ8), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25527|protein.P25527]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=gabP; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=gabP; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=gabP; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=gabP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008763,ECOCYC:EG11330,GeneID:948049`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2794253-2795653:+; feature_type=gene
