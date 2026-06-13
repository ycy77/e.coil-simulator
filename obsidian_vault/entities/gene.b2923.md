---
entity_id: "gene.b2923"
entity_type: "gene"
name: "argO"
source_database: "NCBI RefSeq"
source_id: "gene-b2923"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2923"
  - "argO"
---

# argO

`gene.b2923`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2923`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argO (gene.b2923) is a gene entity. It encodes argO (protein.P11667). Encoded protein function: FUNCTION: Involved in the export of arginine. Important to control the intracellular level of arginine and the correct balance between arginine and lysine. May also be involved in the export of canavanine (a plant-derived antimetabolite). {ECO:0000269|PubMed:15150242}. EcoCyc product frame: YGGA-MONOMER. EcoCyc synonyms: yggA. Genomic coordinates: 3068173-3068808. EcoCyc protein note: ArgO (formerly YggA) is a probable L-arginine efflux transporter in E. coli K-12. Expression of argO is induced by exogenous L-arginine (or the dipeptide Arg-Ala) in an ArgP dependent manner; expression of argO is reduced by L-lysine (or Lys-Ala). Null mutations in either argO or argP result in hypersensitivity to canavanine, a plant derived arginine analog. Overexpression of argO from a plasmid results in increased L-arginine excretion (in an argR mutant strain that has increased intracellular arginine) . ArgO contains 5 predicted transmembrane regions; experimental topology analysis suggests that it adopts an Nin:Cout conformation . ArgO is a member of the LysE family of lysine efflux transporters...

## Biological Role

Repressed by yeiE (protein.P0ACR4). Activated by rpoD (protein.P00579), argP (protein.P0A8S1), lrp (protein.P0ACJ0), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11667|protein.P11667]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=argO; function=+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `C` - regulator=ArgP; target=argO; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=argO; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=argO; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACR4|protein.P0ACR4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009591,ECOCYC:EG11159,GeneID:947418`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3068173-3068808:-; feature_type=gene
