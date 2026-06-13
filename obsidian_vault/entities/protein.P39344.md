---
entity_id: "protein.P39344"
entity_type: "protein"
name: "idnT"
source_database: "UniProt"
source_id: "P39344"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "idnT gntW yjgT b4265 JW4222"
---

# idnT

`protein.P39344`

## Static

- Type: `protein`
- Source: `UniProt:P39344`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Transporter which is probably involved in L-idonate metabolism (PubMed:9658018). Transports L-idonate from the periplasm across the inner membrane (PubMed:9658018). Can also transport D-gluconate and 5-keto-D-gluconate (PubMed:17088549, PubMed:9119199). It has been reported that gluconate uptake probably occurs via a proton-symport mechanism in E.coli (PubMed:4585187). {ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:4585187, ECO:0000269|PubMed:9119199, ECO:0000269|PubMed:9658018}. IdnT is a probable L-idonate and D-gluconate transporter. Originally thought to be a subsidiary gluconate uptake system, the primary role of IdnT appears to be in L-idonate transport. The idnT gene is located in the idnDOTR operon involved in metabolising L-idonate to D-gluconate . Expression of this operon is induced by idonate or by 5-ketogluconate . The cloned idnT gene was shown to confer gluconate transport in a gluconate transport negative mutant in whole cell experiments with IdnT displaying a Km of 60 μM for gluconate . While direct transport of L-idonate has not been shown experimentally, IdnT-mediated gluconate transport is strongly inhibited by idonate . IdnT is a member of the Gnt family of gluconate transporters and is homologous to the E. coli GntT and GntU gluconate transporters. Gluconate uptake has been reported to occur via a proton-symport mechanism in E. coli...

## Biological Role

Catalyzes L-idonate:proton symport (reaction.ecocyc.TRANS-RXN-181A), D-gluconate:proton symport (reaction.ecocyc.TRANS-RXN0-209), 5-ketogluconate:proton symport (reaction.ecocyc.TRANS-RXN0-228). Transports 5-dehydro-D-gluconate (molecule.ecocyc.5-DEHYDROGLUCONATE), L-idonate (molecule.ecocyc.L-IDONATE), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Transporter which is probably involved in L-idonate metabolism (PubMed:9658018). Transports L-idonate from the periplasm across the inner membrane (PubMed:9658018). Can also transport D-gluconate and 5-keto-D-gluconate (PubMed:17088549, PubMed:9119199). It has been reported that gluconate uptake probably occurs via a proton-symport mechanism in E.coli (PubMed:4585187). {ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:4585187, ECO:0000269|PubMed:9119199, ECO:0000269|PubMed:9658018}.

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-181A|reaction.ecocyc.TRANS-RXN-181A]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-209|reaction.ecocyc.TRANS-RXN0-209]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-228|reaction.ecocyc.TRANS-RXN0-228]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.5-DEHYDROGLUCONATE|molecule.ecocyc.5-DEHYDROGLUCONATE]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.L-IDONATE|molecule.ecocyc.L-IDONATE]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4265|gene.b4265]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39344`
- `KEGG:ecj:JW4222;eco:b4265;ecoc:C3026_23005;`
- `GeneID:948798;`
- `GO:GO:0005886; GO:0008643; GO:0015128; GO:0015568; GO:0015726; GO:0019521; GO:0035429; GO:0046183`

## Notes

Gnt-II system L-idonate transporter (L-Ido transporter) (L-idonate transporter) (5-keto-D-gluconate transporter) (L-idonate/5-ketogluconate/gluconate transporter)
