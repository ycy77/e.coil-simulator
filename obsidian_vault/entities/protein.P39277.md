---
entity_id: "protein.P39277"
entity_type: "protein"
name: "yjeH"
source_database: "UniProt"
source_id: "P39277"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:26319875}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjeH b4141 JW4101"
---

# yjeH

`protein.P39277`

## Static

- Type: `protein`
- Source: `UniProt:P39277`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:26319875}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Catalyzes the efflux of L-methionine, L-leucine, L-isoleucine and L-valine (PubMed:26319875). Activity is dependent on electrochemical potential (PubMed:26319875). {ECO:0000269|PubMed:26319875}. yjeH encodes an L-methionine and branched chain amino acid (BCAA) efflux transporter in E. coli K-12. Over-expression of yjeH results in increased tolerance to L-methionine and BCAA structural analogues (DL-ethionine, DL-norleucine, DL-norvaline); over-expression of yjeH is associated with increased export of methionine and the BCAAs when cells are grown in the presence of Met-Met, Ile-Ile, Leu-Leu or Val-Val dipeptides. Additionally, cells lacking yjeH have increased levels of intracellular methionine or BCAAs when grown in the presence of the relevant dipeptides and increased sensitivity to the structural analogues . YjeH efflux activity is dependent on the proton motive force . Expression of yjeH is induced by increased cytoplasmic levels of L-methionine, L-leucine or L-isoleucine; expression of yjeH is not regulated by the transcriptional repressor, PD04032 "MetJ" . YjeH is a member of the Amino Acid Efflux (AAE) Family within the Amino Acid-Polyamine-Organocation (APC) Superfamily of transporters . YjeH is predicted to contain 12 transmembrane α helices, 10 of which form an inverted repeat fold that is characteristic of the APC superfamily

## Biological Role

Catalyzes L-methionine:proton antiport (reaction.ecocyc.RXN0-7050), L-isoleucine:proton antiport (reaction.ecocyc.TRANS-RXN-281), L-valine:proton antiport (reaction.ecocyc.TRANS-RXN-282), L-leucine:proton antiport (reaction.ecocyc.TRANS-RXN0-270). Transports L-Methionine (molecule.C00073), L-Leucine (molecule.C00123), L-Valine (molecule.C00183), L-Isoleucine (molecule.C00407), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Catalyzes the efflux of L-methionine, L-leucine, L-isoleucine and L-valine (PubMed:26319875). Activity is dependent on electrochemical potential (PubMed:26319875). {ECO:0000269|PubMed:26319875}.

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7050|reaction.ecocyc.RXN0-7050]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-281|reaction.ecocyc.TRANS-RXN-281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-282|reaction.ecocyc.TRANS-RXN-282]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-270|reaction.ecocyc.TRANS-RXN0-270]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00123|molecule.C00123]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00407|molecule.C00407]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4141|gene.b4141]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39277`
- `KEGG:ecj:JW4101;eco:b4141;ecoc:C3026_22380;`
- `GeneID:75203976;948656;`
- `GO:GO:0000102; GO:0005294; GO:0005886; GO:0015297; GO:0015820; GO:0015821; GO:0071230; GO:1903714; GO:1903785`

## Notes

L-methionine/branched-chain amino acid exporter YjeH
