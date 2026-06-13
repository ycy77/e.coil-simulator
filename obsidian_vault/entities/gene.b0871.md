---
entity_id: "gene.b0871"
entity_type: "gene"
name: "poxB"
source_database: "NCBI RefSeq"
source_id: "gene-b0871"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0871"
  - "poxB"
---

# poxB

`gene.b0871`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0871`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

poxB (gene.b0871) is a gene entity. It encodes poxB (protein.P07003). Encoded protein function: FUNCTION: A peripheral cell membrane enzyme that catalyzes the oxidative decarboxylation of pyruvate to form acetate and CO(2). It channels electrons from the cytoplasm to the respiratory chain at the cell membrane via ubiquinone (By similarity) (PubMed:18988747, PubMed:2663858, PubMed:365232). The main pathway for acetate production during stationary phase (PubMed:16080684). {ECO:0000255|HAMAP-Rule:MF_00850, ECO:0000269|PubMed:16080684, ECO:0000269|PubMed:18988747, ECO:0000269|PubMed:2663858, ECO:0000269|PubMed:365232}. EcoCyc product frame: PYRUVOXID-MONOMER. Genomic coordinates: 909331-911049. EcoCyc protein note: Pyruvate oxidase is a peripheral membrane enzyme that catalyzes the oxidative decarboxylation of pyruvate to form acetate and CO2. The reaction is coupled to the electron transport chain via ubiquinone. Metabolism of pyruvate by pyruvate oxidase is less efficient than the route via PYRUVATEDEH-CPLX (PDH); however, the pyruvate oxidase route is important for wild-type growth efficiency and responsible for a significant amount of pyruvate metabolism under aerobic conditions . PoxB is the main pathway for acetate production in stationary phase . Under aerobic phosphate starvation conditions, pyruvate flux is diverted from PDH to PoxB, which may decrease oxidative stress...

## Biological Role

Repressed by nsrR (protein.P0AF63). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), oxyR (protein.P0ACQ4), narL (protein.P0AF28), rpoS (protein.P13445).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07003|protein.P07003]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=poxB; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=poxB; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=poxB; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=poxB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=poxB; function=+
- `represses` <-- [[protein.P0AF63|protein.P0AF63]] `RegulonDB` `C` - regulator=NsrR; target=poxB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002958,ECOCYC:EG10754,GeneID:946132`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:909331-911049:-; feature_type=gene
