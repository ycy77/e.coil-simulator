---
entity_id: "gene.b4484"
entity_type: "gene"
name: "cpxP"
source_database: "NCBI RefSeq"
source_id: "gene-b4484"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4484"
  - "cpxP"
---

# cpxP

`gene.b4484`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4484`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cpxP (gene.b4484) is a gene entity. It encodes cpxP (protein.P0AE85). Encoded protein function: FUNCTION: Acts as an auxiliary protein in the Cpx two-component envelope stress response system, helping modulate the Cpx response systems response to some inducers (PubMed:16303867, PubMed:25207645). Binds the periplasmic domain of sensor histidine kinase CpxA, inhibiting induction of the Cpx envelope stress response in the absence of inducer; overexpression decreases Cpx pathway activity (PubMed:16166523, PubMed:21317318). Some periplasmic stimulii (shown for P pili subunit PapE and probably 0.3 M NaCl) increase CpxP's susceptibility to DegP, leading to CpxP degradation, inducing the Cpx pathway (PubMed:16166523, PubMed:16303867). Aids in combating extracytoplasmic protein-mediated toxicity (PubMed:16303867, PubMed:21239493, PubMed:9473036). Overexpression leads to degradation by DegP of misfolded P pili subunits in the periplasm (tested using PapE) (PubMed:21239493). Inhibits autophosphorylation of CpxA in reconstituted liposomes by 50% but has no effect on phosphatase activity of CpxA (PubMed:17259177, PubMed:21239493). Has mild protein chaperone activity (PubMed:21239493, PubMed:21317898)...

## Biological Role

Activated by rpoD (protein.P00579), cpxR (protein.P0AE88), zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE85|protein.P0AE85]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=cpxP; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=cpxP; function=+
- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=cpxP; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0174117,ECOCYC:G7816,GeneID:2847688`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4105820-4106320:+; feature_type=gene
