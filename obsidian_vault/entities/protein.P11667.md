---
entity_id: "protein.P11667"
entity_type: "protein"
name: "argO"
source_database: "UniProt"
source_id: "P11667"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01901, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:27645388}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01901, ECO:0000269|PubMed:27645388}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argO yggA b2923 JW2890"
---

# argO

`protein.P11667`

## Static

- Type: `protein`
- Source: `UniProt:P11667`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01901, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:27645388}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01901, ECO:0000269|PubMed:27645388}.

## Enriched Summary

FUNCTION: Involved in the export of arginine. Important to control the intracellular level of arginine and the correct balance between arginine and lysine. May also be involved in the export of canavanine (a plant-derived antimetabolite). {ECO:0000269|PubMed:15150242}. ArgO (formerly YggA) is a probable L-arginine efflux transporter in E. coli K-12. Expression of argO is induced by exogenous L-arginine (or the dipeptide Arg-Ala) in an ArgP dependent manner; expression of argO is reduced by L-lysine (or Lys-Ala). Null mutations in either argO or argP result in hypersensitivity to canavanine, a plant derived arginine analog. Overexpression of argO from a plasmid results in increased L-arginine excretion (in an argR mutant strain that has increased intracellular arginine) . ArgO contains 5 predicted transmembrane regions; experimental topology analysis suggests that it adopts an Nin:Cout conformation . ArgO is a member of the LysE family of lysine efflux transporters . ArgO has a latent capacity for lysine efflux; overexpression of argO alleviates the growth defect of a lysO::Kan mutant under cytoplasmic lysine stress and restores some thialysine resistance to an argO lysO double null mutant . argO: arginine outward transport"

## Biological Role

Catalyzes RXN66-448 (reaction.ecocyc.RXN66-448), TRANS-RXN-325 (reaction.ecocyc.TRANS-RXN-325).

## Annotation

FUNCTION: Involved in the export of arginine. Important to control the intracellular level of arginine and the correct balance between arginine and lysine. May also be involved in the export of canavanine (a plant-derived antimetabolite). {ECO:0000269|PubMed:15150242}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN66-448|reaction.ecocyc.RXN66-448]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-325|reaction.ecocyc.TRANS-RXN-325]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2923|gene.b2923]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11667`
- `KEGG:ecj:JW2890;eco:b2923;`
- `GeneID:947418;`
- `GO:GO:0005886; GO:0006865; GO:0015171; GO:0061459; GO:1903826`

## Notes

Arginine exporter protein ArgO
