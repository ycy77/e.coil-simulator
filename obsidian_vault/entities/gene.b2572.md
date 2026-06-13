---
entity_id: "gene.b2572"
entity_type: "gene"
name: "rseA"
source_database: "NCBI RefSeq"
source_id: "gene-b2572"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2572"
  - "rseA"
---

# rseA

`gene.b2572`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2572`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rseA (gene.b2572) is a gene entity. It encodes rseA (protein.P0AFX7). Encoded protein function: FUNCTION: An anti-sigma factor for extracytoplasmic function (ECF) sigma factor sigma-E (RpoE). ECF sigma factors are held in an inactive form by an anti-sigma factor until released by regulated intramembrane proteolysis (RIP). RIP occurs when an extracytoplasmic signal triggers a concerted proteolytic cascade to transmit information and elicit cellular responses. The membrane-spanning regulatory substrate protein is first cut periplasmically (site-1 protease, S1P, DegS), then within the membrane itself (site-2 protease, S2P, RseP), while cytoplasmic proteases finish degrading the anti-sigma factor, liberating sigma-E. Overexpression of RseA blocks sigma-E from acting, results in cell lysis in stationary phase and temperature-sensitivity above 37 degrees Celsius. {ECO:0000269|PubMed:23687042, ECO:0000269|PubMed:9159522, ECO:0000269|PubMed:9159523}. EcoCyc product frame: EG12341-MONOMER. EcoCyc synonyms: yfiJ, mclA. Genomic coordinates: 2708754-2709404. EcoCyc protein note: RseA is an anti-sigma factor that inhibits σE . RseA is the major regulator of σE . RseA associates with the region of σE that interacts with DNA and may interfere with promoter binding . Structural studies indicate that RseA interferes with binding of σE to core polymerase...

## Biological Role

Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), crp (protein.P0ACJ8), glnG (protein.P0AFB8), glrR (protein.P0AFU4), rpoE (protein.P0AGB6), rcsB (protein.P0DMC7), rpoS (protein.P13445), and 1 more.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFX7|protein.P0AFX7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rseA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rseA; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rseA; function=+
- `activates` <-- [[protein.P0AFU4|protein.P0AFU4]] `RegulonDB` `S` - regulator=GlrR; target=rseA; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=rseA; function=+
- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `C` - regulator=RcsB; target=rseA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=rseA; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=rseA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008462,ECOCYC:EG12341,GeneID:947053`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2708754-2709404:-; feature_type=gene
