---
entity_id: "protein.P75826"
entity_type: "protein"
name: "lysO"
source_database: "UniProt"
source_id: "P75826"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lysO ybjE b0874 JW0858"
---

# lysO

`protein.P75826`

## Static

- Type: `protein`
- Source: `UniProt:P75826`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Mediates export of lysine. {ECO:0000269|PubMed:25845847}. LysO is an L-lysine/thialysine efflux transporter. A ΔlysO strain has an increased intracellular concentration of L-lysine and impaired growth in the presence of the dipeptide Lys-Ala (but not in the presence of Arg-Ala); a ΔlysO strain is sensitive to the naturally occurring lysine antimetabolite, thialysine . LysO may export thialysine with higher affinity than L-lysine; LysO exports thialysine via proton-coupled antiport . Overexpression of lysO from a plasmid mediates increased export of L-lysine in Lys-Ala containing medium and mediates increased resistance to thialysine; overexpression of lysO from a plasmid suppresses the canavanine supersensitive phenotype of a strain lacking the arginine efflux transporter, ArgO possibly because increased extracellular lysine inhibits canavanine uptake by the ABC-3-CPLX . The cis-regulatory region of lysO contains an imperfect ArgR binding site; arginine mediates transcriptional repression of lysO via the ArgR repressor however this effect may only be evident when the cytoplasmic level of arginine is high . LysO contains 8 transmembrane regions and adopts an Nout-Cout configuration in the cytoplasmic membrane . Enhanced expression of lysO (formerly ybjE) results in accumulation of specific L-amino acids in the culture medium of E...

## Biological Role

Catalyzes L-lysine:H+ antiport (reaction.ecocyc.TRANS-RXN-401), TRANS-RXN-492 (reaction.ecocyc.TRANS-RXN-492). Transports L-Lysine (molecule.C00047), hν (molecule.ecocyc.Light), S-(2-aminoethyl)-L-cysteine (molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE).

## Annotation

FUNCTION: Mediates export of lysine. {ECO:0000269|PubMed:25845847}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-401|reaction.ecocyc.TRANS-RXN-401]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-492|reaction.ecocyc.TRANS-RXN-492]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00047|molecule.C00047]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE|molecule.ecocyc.S-2-AMINOETHYL-L-CYSTEINE]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0874|gene.b0874]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75826`
- `KEGG:ecj:JW0858;eco:b0874;ecoc:C3026_05430;`
- `GeneID:93776547;947142;`
- `GO:GO:0005886; GO:0015661; GO:1903401`

## Notes

Lysine exporter LysO (Lys outward permease)
