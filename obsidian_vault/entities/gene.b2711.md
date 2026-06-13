---
entity_id: "gene.b2711"
entity_type: "gene"
name: "norW"
source_database: "NCBI RefSeq"
source_id: "gene-b2711"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2711"
  - "norW"
---

# norW

`gene.b2711`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2711`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

norW (gene.b2711) is a gene entity. It encodes norW (protein.P37596). Encoded protein function: FUNCTION: One of at least two accessory proteins for anaerobic nitric oxide (NO) reductase. Reduces the rubredoxin moiety of NO reductase. EcoCyc product frame: EG12450-MONOMER. EcoCyc synonyms: ygaL, ygbD. Genomic coordinates: 2833912-2835045. EcoCyc protein note: The CPLX0-1 NorV/NorW system constitutes a nitric oxide reductase that couples NADH oxidation to NO reduction . The electron transfer chain begins with NADH oxidation by NorW, which then transfers the electron to the rubredoxin domain of NorV. Electrons travel through the protein to the catalytic di-iron site, where they are used for reduction of NO to N2O. NorW is a flavorubredoxin reductase that converts the oxidized form of the flavorubredoxin (NorV) electron carrier to its reduced form . The redox properties of NorW have been characterized , and the kinetics of electron transfer from NADH via NorW and NorV to NO has been measured . Partially purified NorW also shows some tellurite reductase activity with NADH as the electron donor . Nitric oxide has been shown to have diverse biologial functions; however, the molecule also inactivates essential cellular enzymes. It is therefore essential that NO is removed from the cell. A kinetic model of the fate of NO within E. coli has been constructed and tested...

## Biological Role

Activated by rpoN (protein.P24255), norR (protein.P37013).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37596|protein.P37596]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=norW; function=+
- `activates` <-- [[protein.P37013|protein.P37013]] `RegulonDB` `C` - regulator=NorR; target=norW; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008912,ECOCYC:EG12450,GeneID:947088`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2833912-2835045:+; feature_type=gene
