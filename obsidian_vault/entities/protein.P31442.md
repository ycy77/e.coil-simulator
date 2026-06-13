---
entity_id: "protein.P31442"
entity_type: "protein"
name: "emrD"
source_database: "UniProt"
source_id: "P31442"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "emrD yicQ b3673 JW5634"
---

# emrD

`protein.P31442`

## Static

- Type: `protein`
- Source: `UniProt:P31442`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Multidrug resistance pump that participates in a low energy shock adaptive response. EmrD is implicated in the adaptive response to uncouplers of oxidative phosphorylation: disruption of emrD via transposon mutagenesis results in increased sensitivity to carbonyl cyanide m-chlorophenylhydrazone (CCCP) and tetrachlorosalicylanilide (TSA) compared to wild type; emrD expression is induced by uncouplers and is subject to catabolite repression . emrD encodes a putative 12 α-helix transmembrane translocase . Multicopy expression of emrD in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ), confers increased resistance to SDS and benzalkonium but does not impact the resistance to a range of other antibiotics and toxic compounds including CCCP . Purified EmrD binds Hoechst33342 and doxorubicin with micromolar affinity; EmrD transports Hoechst weakly and expression of emrD in a drug-sensitive background (ΔacrAB ΔemrE ΔmdfA) does not confer increased resistance to benzalkonium chloride, CCCP, doxorubicin or Hoechst3334 . In the 3.5Å crystal structure of EmrD, the 12 transmembrane helices form a structure that spans the lipid bilayer and contains an internal cavity of mostly hydrophobic residues; EmrD may intercept CCCP on the inner leaflet of the membrane as it crosses toward the cytoplasm...

## Biological Role

Catalyzes carbonylcyanide m-chlorophenylhydrazone:proton antiport (reaction.ecocyc.TRANS-RXN-339), xenobiotic:proton antiport (reaction.ecocyc.TRANS-RXN-44). Transports carbonylcyanide m-chlorophenylhydrazone (molecule.ecocyc.CPD-7970), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Multidrug resistance pump that participates in a low energy shock adaptive response.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-339|reaction.ecocyc.TRANS-RXN-339]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-44|reaction.ecocyc.TRANS-RXN-44]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3673|gene.b3673]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31442`
- `KEGG:ecj:JW5634;eco:b3673;ecoc:C3026_19920;`
- `GeneID:75205388;948180;`
- `GO:GO:0005886; GO:0022857; GO:0042910; GO:1990961`

## Notes

Multidrug resistance protein D
